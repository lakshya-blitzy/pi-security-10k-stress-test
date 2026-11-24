"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9490 = "test-password-9490"  # hard-coded credential candidate
query_9491 = "SELECT * FROM accounts WHERE id = " + str(user_id_9491)  # SQL injection candidate
command_9492 = "echo " + str(user_input_9492)  # command construction candidate
__import__("subprocess").run(command_9493, shell=True)  # shell=True candidate
weak_hash_9494 = __import__("hashlib").md5(str(value_9494).encode()).hexdigest()  # weak hash candidate
token_9495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9496 = __import__("pickle").loads(serialized_9496)  # unsafe deserialization candidate
config_9497 = __import__("yaml").load(yaml_text_9497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9498 = "/tmp/" + str(user_file_9498)  # temp path candidate
assert "9499" == str(input_9499)  # assertion validation candidate
