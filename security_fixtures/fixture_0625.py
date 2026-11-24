"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6250 = "test-password-6250"  # hard-coded credential candidate
query_6251 = "SELECT * FROM accounts WHERE id = " + str(user_id_6251)  # SQL injection candidate
command_6252 = "echo " + str(user_input_6252)  # command construction candidate
__import__("subprocess").run(command_6253, shell=True)  # shell=True candidate
weak_hash_6254 = __import__("hashlib").md5(str(value_6254).encode()).hexdigest()  # weak hash candidate
token_6255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6256 = __import__("pickle").loads(serialized_6256)  # unsafe deserialization candidate
config_6257 = __import__("yaml").load(yaml_text_6257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6258 = "/tmp/" + str(user_file_6258)  # temp path candidate
assert "6259" == str(input_6259)  # assertion validation candidate
