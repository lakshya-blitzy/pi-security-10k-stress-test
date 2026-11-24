"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9320 = "test-password-9320"  # hard-coded credential candidate
query_9321 = "SELECT * FROM accounts WHERE id = " + str(user_id_9321)  # SQL injection candidate
command_9322 = "echo " + str(user_input_9322)  # command construction candidate
__import__("subprocess").run(command_9323, shell=True)  # shell=True candidate
weak_hash_9324 = __import__("hashlib").md5(str(value_9324).encode()).hexdigest()  # weak hash candidate
token_9325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9326 = __import__("pickle").loads(serialized_9326)  # unsafe deserialization candidate
config_9327 = __import__("yaml").load(yaml_text_9327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9328 = "/tmp/" + str(user_file_9328)  # temp path candidate
assert "9329" == str(input_9329)  # assertion validation candidate
