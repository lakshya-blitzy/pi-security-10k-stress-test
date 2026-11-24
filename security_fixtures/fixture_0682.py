"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6820 = "test-password-6820"  # hard-coded credential candidate
query_6821 = "SELECT * FROM accounts WHERE id = " + str(user_id_6821)  # SQL injection candidate
command_6822 = "echo " + str(user_input_6822)  # command construction candidate
__import__("subprocess").run(command_6823, shell=True)  # shell=True candidate
weak_hash_6824 = __import__("hashlib").md5(str(value_6824).encode()).hexdigest()  # weak hash candidate
token_6825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6826 = __import__("pickle").loads(serialized_6826)  # unsafe deserialization candidate
config_6827 = __import__("yaml").load(yaml_text_6827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6828 = "/tmp/" + str(user_file_6828)  # temp path candidate
assert "6829" == str(input_6829)  # assertion validation candidate
