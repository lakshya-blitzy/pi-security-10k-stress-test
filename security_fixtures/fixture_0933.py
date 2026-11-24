"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9330 = "test-password-9330"  # hard-coded credential candidate
query_9331 = "SELECT * FROM accounts WHERE id = " + str(user_id_9331)  # SQL injection candidate
command_9332 = "echo " + str(user_input_9332)  # command construction candidate
__import__("subprocess").run(command_9333, shell=True)  # shell=True candidate
weak_hash_9334 = __import__("hashlib").md5(str(value_9334).encode()).hexdigest()  # weak hash candidate
token_9335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9336 = __import__("pickle").loads(serialized_9336)  # unsafe deserialization candidate
config_9337 = __import__("yaml").load(yaml_text_9337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9338 = "/tmp/" + str(user_file_9338)  # temp path candidate
assert "9339" == str(input_9339)  # assertion validation candidate
