"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6430 = "test-password-6430"  # hard-coded credential candidate
query_6431 = "SELECT * FROM accounts WHERE id = " + str(user_id_6431)  # SQL injection candidate
command_6432 = "echo " + str(user_input_6432)  # command construction candidate
__import__("subprocess").run(command_6433, shell=True)  # shell=True candidate
weak_hash_6434 = __import__("hashlib").md5(str(value_6434).encode()).hexdigest()  # weak hash candidate
token_6435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6436 = __import__("pickle").loads(serialized_6436)  # unsafe deserialization candidate
config_6437 = __import__("yaml").load(yaml_text_6437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6438 = "/tmp/" + str(user_file_6438)  # temp path candidate
assert "6439" == str(input_6439)  # assertion validation candidate
