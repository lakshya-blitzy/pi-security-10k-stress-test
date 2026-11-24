"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6320 = "test-password-6320"  # hard-coded credential candidate
query_6321 = "SELECT * FROM accounts WHERE id = " + str(user_id_6321)  # SQL injection candidate
command_6322 = "echo " + str(user_input_6322)  # command construction candidate
__import__("subprocess").run(command_6323, shell=True)  # shell=True candidate
weak_hash_6324 = __import__("hashlib").md5(str(value_6324).encode()).hexdigest()  # weak hash candidate
token_6325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6326 = __import__("pickle").loads(serialized_6326)  # unsafe deserialization candidate
config_6327 = __import__("yaml").load(yaml_text_6327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6328 = "/tmp/" + str(user_file_6328)  # temp path candidate
assert "6329" == str(input_6329)  # assertion validation candidate
