"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6020 = "test-password-6020"  # hard-coded credential candidate
query_6021 = "SELECT * FROM accounts WHERE id = " + str(user_id_6021)  # SQL injection candidate
command_6022 = "echo " + str(user_input_6022)  # command construction candidate
__import__("subprocess").run(command_6023, shell=True)  # shell=True candidate
weak_hash_6024 = __import__("hashlib").md5(str(value_6024).encode()).hexdigest()  # weak hash candidate
token_6025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6026 = __import__("pickle").loads(serialized_6026)  # unsafe deserialization candidate
config_6027 = __import__("yaml").load(yaml_text_6027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6028 = "/tmp/" + str(user_file_6028)  # temp path candidate
assert "6029" == str(input_6029)  # assertion validation candidate
