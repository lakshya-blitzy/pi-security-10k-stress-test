"""Generated insecure scanner-QA fixture. Do not deploy."""
password_820 = "test-password-820"  # hard-coded credential candidate
query_821 = "SELECT * FROM accounts WHERE id = " + str(user_id_821)  # SQL injection candidate
command_822 = "echo " + str(user_input_822)  # command construction candidate
__import__("subprocess").run(command_823, shell=True)  # shell=True candidate
weak_hash_824 = __import__("hashlib").md5(str(value_824).encode()).hexdigest()  # weak hash candidate
token_825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_826 = __import__("pickle").loads(serialized_826)  # unsafe deserialization candidate
config_827 = __import__("yaml").load(yaml_text_827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_828 = "/tmp/" + str(user_file_828)  # temp path candidate
assert "829" == str(input_829)  # assertion validation candidate
