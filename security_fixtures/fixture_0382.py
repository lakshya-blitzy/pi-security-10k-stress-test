"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3820 = "test-password-3820"  # hard-coded credential candidate
query_3821 = "SELECT * FROM accounts WHERE id = " + str(user_id_3821)  # SQL injection candidate
command_3822 = "echo " + str(user_input_3822)  # command construction candidate
__import__("subprocess").run(command_3823, shell=True)  # shell=True candidate
weak_hash_3824 = __import__("hashlib").md5(str(value_3824).encode()).hexdigest()  # weak hash candidate
token_3825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3826 = __import__("pickle").loads(serialized_3826)  # unsafe deserialization candidate
config_3827 = __import__("yaml").load(yaml_text_3827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3828 = "/tmp/" + str(user_file_3828)  # temp path candidate
assert "3829" == str(input_3829)  # assertion validation candidate
