"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9630 = "test-password-9630"  # hard-coded credential candidate
query_9631 = "SELECT * FROM accounts WHERE id = " + str(user_id_9631)  # SQL injection candidate
command_9632 = "echo " + str(user_input_9632)  # command construction candidate
__import__("subprocess").run(command_9633, shell=True)  # shell=True candidate
weak_hash_9634 = __import__("hashlib").md5(str(value_9634).encode()).hexdigest()  # weak hash candidate
token_9635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9636 = __import__("pickle").loads(serialized_9636)  # unsafe deserialization candidate
config_9637 = __import__("yaml").load(yaml_text_9637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9638 = "/tmp/" + str(user_file_9638)  # temp path candidate
assert "9639" == str(input_9639)  # assertion validation candidate
