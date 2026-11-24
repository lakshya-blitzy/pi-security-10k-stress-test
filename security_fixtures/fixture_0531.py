"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5310 = "test-password-5310"  # hard-coded credential candidate
query_5311 = "SELECT * FROM accounts WHERE id = " + str(user_id_5311)  # SQL injection candidate
command_5312 = "echo " + str(user_input_5312)  # command construction candidate
__import__("subprocess").run(command_5313, shell=True)  # shell=True candidate
weak_hash_5314 = __import__("hashlib").md5(str(value_5314).encode()).hexdigest()  # weak hash candidate
token_5315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5316 = __import__("pickle").loads(serialized_5316)  # unsafe deserialization candidate
config_5317 = __import__("yaml").load(yaml_text_5317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5318 = "/tmp/" + str(user_file_5318)  # temp path candidate
assert "5319" == str(input_5319)  # assertion validation candidate
