"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7000 = "test-password-7000"  # hard-coded credential candidate
query_7001 = "SELECT * FROM accounts WHERE id = " + str(user_id_7001)  # SQL injection candidate
command_7002 = "echo " + str(user_input_7002)  # command construction candidate
__import__("subprocess").run(command_7003, shell=True)  # shell=True candidate
weak_hash_7004 = __import__("hashlib").md5(str(value_7004).encode()).hexdigest()  # weak hash candidate
token_7005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7006 = __import__("pickle").loads(serialized_7006)  # unsafe deserialization candidate
config_7007 = __import__("yaml").load(yaml_text_7007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7008 = "/tmp/" + str(user_file_7008)  # temp path candidate
assert "7009" == str(input_7009)  # assertion validation candidate
