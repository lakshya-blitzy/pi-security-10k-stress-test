"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6310 = "test-password-6310"  # hard-coded credential candidate
query_6311 = "SELECT * FROM accounts WHERE id = " + str(user_id_6311)  # SQL injection candidate
command_6312 = "echo " + str(user_input_6312)  # command construction candidate
__import__("subprocess").run(command_6313, shell=True)  # shell=True candidate
weak_hash_6314 = __import__("hashlib").md5(str(value_6314).encode()).hexdigest()  # weak hash candidate
token_6315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6316 = __import__("pickle").loads(serialized_6316)  # unsafe deserialization candidate
config_6317 = __import__("yaml").load(yaml_text_6317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6318 = "/tmp/" + str(user_file_6318)  # temp path candidate
assert "6319" == str(input_6319)  # assertion validation candidate
