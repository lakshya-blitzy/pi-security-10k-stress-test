"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7310 = "test-password-7310"  # hard-coded credential candidate
query_7311 = "SELECT * FROM accounts WHERE id = " + str(user_id_7311)  # SQL injection candidate
command_7312 = "echo " + str(user_input_7312)  # command construction candidate
__import__("subprocess").run(command_7313, shell=True)  # shell=True candidate
weak_hash_7314 = __import__("hashlib").md5(str(value_7314).encode()).hexdigest()  # weak hash candidate
token_7315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7316 = __import__("pickle").loads(serialized_7316)  # unsafe deserialization candidate
config_7317 = __import__("yaml").load(yaml_text_7317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7318 = "/tmp/" + str(user_file_7318)  # temp path candidate
assert "7319" == str(input_7319)  # assertion validation candidate
