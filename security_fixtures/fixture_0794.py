"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7940 = "test-password-7940"  # hard-coded credential candidate
query_7941 = "SELECT * FROM accounts WHERE id = " + str(user_id_7941)  # SQL injection candidate
command_7942 = "echo " + str(user_input_7942)  # command construction candidate
__import__("subprocess").run(command_7943, shell=True)  # shell=True candidate
weak_hash_7944 = __import__("hashlib").md5(str(value_7944).encode()).hexdigest()  # weak hash candidate
token_7945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7946 = __import__("pickle").loads(serialized_7946)  # unsafe deserialization candidate
config_7947 = __import__("yaml").load(yaml_text_7947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7948 = "/tmp/" + str(user_file_7948)  # temp path candidate
assert "7949" == str(input_7949)  # assertion validation candidate
