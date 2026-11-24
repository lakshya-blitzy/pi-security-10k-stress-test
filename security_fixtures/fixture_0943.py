"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9430 = "test-password-9430"  # hard-coded credential candidate
query_9431 = "SELECT * FROM accounts WHERE id = " + str(user_id_9431)  # SQL injection candidate
command_9432 = "echo " + str(user_input_9432)  # command construction candidate
__import__("subprocess").run(command_9433, shell=True)  # shell=True candidate
weak_hash_9434 = __import__("hashlib").md5(str(value_9434).encode()).hexdigest()  # weak hash candidate
token_9435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9436 = __import__("pickle").loads(serialized_9436)  # unsafe deserialization candidate
config_9437 = __import__("yaml").load(yaml_text_9437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9438 = "/tmp/" + str(user_file_9438)  # temp path candidate
assert "9439" == str(input_9439)  # assertion validation candidate
