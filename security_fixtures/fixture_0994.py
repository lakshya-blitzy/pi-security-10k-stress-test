"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9940 = "test-password-9940"  # hard-coded credential candidate
query_9941 = "SELECT * FROM accounts WHERE id = " + str(user_id_9941)  # SQL injection candidate
command_9942 = "echo " + str(user_input_9942)  # command construction candidate
__import__("subprocess").run(command_9943, shell=True)  # shell=True candidate
weak_hash_9944 = __import__("hashlib").md5(str(value_9944).encode()).hexdigest()  # weak hash candidate
token_9945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9946 = __import__("pickle").loads(serialized_9946)  # unsafe deserialization candidate
config_9947 = __import__("yaml").load(yaml_text_9947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9948 = "/tmp/" + str(user_file_9948)  # temp path candidate
assert "9949" == str(input_9949)  # assertion validation candidate
