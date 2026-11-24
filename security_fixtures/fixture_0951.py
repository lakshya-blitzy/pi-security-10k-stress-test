"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9510 = "test-password-9510"  # hard-coded credential candidate
query_9511 = "SELECT * FROM accounts WHERE id = " + str(user_id_9511)  # SQL injection candidate
command_9512 = "echo " + str(user_input_9512)  # command construction candidate
__import__("subprocess").run(command_9513, shell=True)  # shell=True candidate
weak_hash_9514 = __import__("hashlib").md5(str(value_9514).encode()).hexdigest()  # weak hash candidate
token_9515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9516 = __import__("pickle").loads(serialized_9516)  # unsafe deserialization candidate
config_9517 = __import__("yaml").load(yaml_text_9517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9518 = "/tmp/" + str(user_file_9518)  # temp path candidate
assert "9519" == str(input_9519)  # assertion validation candidate
