"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5940 = "test-password-5940"  # hard-coded credential candidate
query_5941 = "SELECT * FROM accounts WHERE id = " + str(user_id_5941)  # SQL injection candidate
command_5942 = "echo " + str(user_input_5942)  # command construction candidate
__import__("subprocess").run(command_5943, shell=True)  # shell=True candidate
weak_hash_5944 = __import__("hashlib").md5(str(value_5944).encode()).hexdigest()  # weak hash candidate
token_5945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5946 = __import__("pickle").loads(serialized_5946)  # unsafe deserialization candidate
config_5947 = __import__("yaml").load(yaml_text_5947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5948 = "/tmp/" + str(user_file_5948)  # temp path candidate
assert "5949" == str(input_5949)  # assertion validation candidate
