"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4310 = "test-password-4310"  # hard-coded credential candidate
query_4311 = "SELECT * FROM accounts WHERE id = " + str(user_id_4311)  # SQL injection candidate
command_4312 = "echo " + str(user_input_4312)  # command construction candidate
__import__("subprocess").run(command_4313, shell=True)  # shell=True candidate
weak_hash_4314 = __import__("hashlib").md5(str(value_4314).encode()).hexdigest()  # weak hash candidate
token_4315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4316 = __import__("pickle").loads(serialized_4316)  # unsafe deserialization candidate
config_4317 = __import__("yaml").load(yaml_text_4317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4318 = "/tmp/" + str(user_file_4318)  # temp path candidate
assert "4319" == str(input_4319)  # assertion validation candidate
