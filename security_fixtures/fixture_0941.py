"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9410 = "test-password-9410"  # hard-coded credential candidate
query_9411 = "SELECT * FROM accounts WHERE id = " + str(user_id_9411)  # SQL injection candidate
command_9412 = "echo " + str(user_input_9412)  # command construction candidate
__import__("subprocess").run(command_9413, shell=True)  # shell=True candidate
weak_hash_9414 = __import__("hashlib").md5(str(value_9414).encode()).hexdigest()  # weak hash candidate
token_9415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9416 = __import__("pickle").loads(serialized_9416)  # unsafe deserialization candidate
config_9417 = __import__("yaml").load(yaml_text_9417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9418 = "/tmp/" + str(user_file_9418)  # temp path candidate
assert "9419" == str(input_9419)  # assertion validation candidate
